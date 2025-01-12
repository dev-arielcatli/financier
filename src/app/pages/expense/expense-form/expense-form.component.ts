import { Component, inject } from '@angular/core';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatIconModule } from '@angular/material/icon';
import { COMMA, ENTER } from '@angular/cdk/keycodes';

import {
  MAT_DIALOG_DATA,
  MatDialogActions,
  MatDialogRef,
} from '@angular/material/dialog';
import { MatButtonModule } from '@angular/material/button';
import {
  MatChipEditedEvent,
  MatChipInputEvent,
  MatChipsModule,
} from '@angular/material/chips';
import { CommonModule } from '@angular/common';
import { SafeDisplayExpense } from '../../../store/expense/expense.model';

@Component({
  selector: 'fn-expense-form',
  imports: [
    ReactiveFormsModule,
    MatFormFieldModule,
    MatInputModule,
    MatDialogActions,
    MatButtonModule,
    MatIconModule,
    MatChipsModule,
    CommonModule,
  ],
  templateUrl: './expense-form.component.html',
  styleUrl: './expense-form.component.scss',
})
export class ExpenseFormComponent {
  private formBuilder = inject(FormBuilder);

  expenseDialogRef = inject(MatDialogRef<ExpenseFormComponent>);

  dialogData: SafeDisplayExpense = inject(MAT_DIALOG_DATA);

  expenseForm = this.formBuilder.group({
    id: [''],
    name: ['', Validators.required],
    description: [''],
    quantity: [1],
    amount: [0],
    date: [new Date()],
    createdAt: [new Date()],
    updatedAt: [new Date()],
    address: [''],
    tags: [[]],
  });

  // CHIPS
  readonly separatorKeysCodes = [ENTER, COMMA] as const;

  constructor() {
    if (this.dialogData) {
      this.expenseForm.patchValue(this.dialogData);
    }
  }

  get tags(): string[] {
    return this.expenseForm.value.tags || [];
  }

  onSave(): void {
    if (this.expenseForm.valid) {
      this.expenseDialogRef.close(this.expenseForm.value);
    }
  }

  onCancel(): void {
    this.expenseDialogRef.close();
  }

  addTag(event: MatChipInputEvent): void {
    const newTag = (event.value || '').trim();
    if (newTag) {
      this.expenseForm.controls.tags.patchValue(
        // TODO: Fix issue with this model
        this.tags.concat(newTag) as any,
      );
    }
    event.chipInput!.clear();
  }

  removeTag(tag: string): void {
    this.expenseForm.controls.tags.patchValue(
      // TODO: Fix issue with this model
      this.tags.filter((t) => t !== tag) as any,
    );
  }
}
