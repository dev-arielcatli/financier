import {
  AfterViewInit,
  Component,
  computed,
  inject,
  Signal,
  signal,
  ViewChild,
} from '@angular/core';
import { ReactiveFormsModule } from '@angular/forms';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatTableDataSource, MatTableModule } from '@angular/material/table';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';

import { MatInputModule } from '@angular/material/input';
import {
  MatDialog,
  MatDialogModule,
  MatDialogRef,
} from '@angular/material/dialog';
import { IncomeFormComponent } from './income-form/income-form.component';
import { mockIncomes } from './mocks/incomes.mock';
import { CommonModule } from '@angular/common';

import { MatPaginator, MatPaginatorModule } from '@angular/material/paginator';
import { ShortenPipe } from '../../shared/shortener.pipe';
import { MatSortModule } from '@angular/material/sort';
import { Income, SafeDisplayIncome } from './income.model';

@Component({
  selector: 'fn-income',
  imports: [
    CommonModule,
    ReactiveFormsModule,
    MatFormFieldModule,
    MatInputModule,
    MatDialogModule,
    MatTableModule,
    MatPaginatorModule,
    ShortenPipe,
    MatButtonModule,
    MatIconModule,
    MatSortModule,
  ],
  templateUrl: './income.component.html',
  styleUrl: './income.component.scss',
})
export class IncomeComponent implements AfterViewInit {
  @ViewChild(MatPaginator) incomeTablePaginator!: MatPaginator;

  incomeDialog = inject(MatDialog);
  incomeDialogRef!: MatDialogRef<IncomeFormComponent>;

  INCOME_COLUMNS: string[] = [
    'name',
    'description',
    'quantity',
    'amount',
    'date',
  ];

  private rawIncomes = signal<Income[]>(mockIncomes);
  incomes: Signal<SafeDisplayIncome[]> = computed(() => {
    const formattedIncomes = this.formatIncomes(this.rawIncomes());
    this.incomeDataSource = new MatTableDataSource<SafeDisplayIncome>(
      formattedIncomes,
    );
    return formattedIncomes;
  });

  incomeDataSource = new MatTableDataSource<SafeDisplayIncome>([]);

  ngAfterViewInit(): void {
    // TODO: computed() signals are only computed when they are accessed.
    this.incomes();
    this.incomeDataSource.paginator = this.incomeTablePaginator;
  }

  onAddIncome(): void {
    this.incomeDialogRef = this.incomeDialog.open(IncomeFormComponent, {});
    this.subscribeToIncomeDialogClose();
  }

  private formatIncomes(incomes: Income[]): SafeDisplayIncome[] {
    return incomes.map((income) => {
      return {
        ...income,
        date: new Date(income.date).toLocaleString('en-US', {
          weekday: 'long',
          day: 'numeric',
          month: 'long',
          year: 'numeric',
          hour: 'numeric',
          minute: 'numeric',
          hour12: true,
        }),
        createdAt: new Date(income.createdAt).toLocaleString('en-US', {
          weekday: 'long',
          day: 'numeric',
          month: 'long',
          year: 'numeric',
          hour: 'numeric',
          minute: 'numeric',
          hour12: true,
        }),
        updatedAt: new Date(income.updatedAt).toLocaleString('en-US', {
          weekday: 'long',
          day: 'numeric',
          month: 'long',
          year: 'numeric',
          hour: 'numeric',
          minute: 'numeric',
          hour12: true,
        }),
      };
    });
  }

  private onIncomeDialogClose(income: Income): void {
    if (income) {
      if (income.id) {
        console.log('Update income', income);
      } else {
        console.log('Create income', income);
      }
    }
  }

  subscribeToIncomeDialogClose(): void {
    this.incomeDialogRef.afterClosed().subscribe((payload) => {
      this.onIncomeDialogClose(payload);
    });
  }

  onRowClick(income: Income): void {
    this.incomeDialogRef = this.incomeDialog.open(IncomeFormComponent, {
      data: income,
    });
    this.subscribeToIncomeDialogClose();
  }
}
