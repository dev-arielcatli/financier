import { Component, inject } from '@angular/core';
import { FormBuilder, ReactiveFormsModule } from '@angular/forms';
import { Expense } from './expense.model';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';

@Component({
  selector: 'fn-expense',
  imports: [ReactiveFormsModule, MatFormFieldModule, MatInputModule],
  templateUrl: './expense.component.html',
  styleUrl: './expense.component.scss',
})
export class ExpenseComponent {
  private formBuilder = inject(FormBuilder);

  expenseForm = this.formBuilder.group<Expense>({
    id: '',
    name: '',
    description: '',
    quantity: 0,
    amount: 0,
    date: new Date(),
    createdAt: new Date(),
    updatedAt: new Date(),
    address: '',
    tags: [],
  });
}
